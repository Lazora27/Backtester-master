import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
