import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
