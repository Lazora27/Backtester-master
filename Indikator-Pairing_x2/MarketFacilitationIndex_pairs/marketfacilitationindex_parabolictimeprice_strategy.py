import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
