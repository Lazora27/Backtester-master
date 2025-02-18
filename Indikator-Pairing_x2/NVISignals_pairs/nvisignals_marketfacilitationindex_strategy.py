import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
