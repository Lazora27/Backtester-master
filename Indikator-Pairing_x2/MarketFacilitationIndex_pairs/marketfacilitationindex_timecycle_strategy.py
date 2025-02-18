import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
