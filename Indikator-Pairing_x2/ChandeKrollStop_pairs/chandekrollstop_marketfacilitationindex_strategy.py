import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
