import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
