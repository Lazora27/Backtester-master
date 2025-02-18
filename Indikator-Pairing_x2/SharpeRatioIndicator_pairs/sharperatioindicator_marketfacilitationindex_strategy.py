import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
