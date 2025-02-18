import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
