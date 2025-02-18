import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
