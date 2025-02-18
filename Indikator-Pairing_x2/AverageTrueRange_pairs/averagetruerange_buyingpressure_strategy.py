import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BuyingPressure': 1.0
        })
    )
