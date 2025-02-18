import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_HilbertPhaseIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und HilbertPhaseIndicator
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'HilbertPhaseIndicator': 1.0
        })
    )
