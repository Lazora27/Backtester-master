import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
