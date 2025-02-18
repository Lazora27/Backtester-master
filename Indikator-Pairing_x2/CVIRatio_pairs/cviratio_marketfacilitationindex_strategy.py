import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
