import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HullMovingAverage': 1.0
        })
    )
