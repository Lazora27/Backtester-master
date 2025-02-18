import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
