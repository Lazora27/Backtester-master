import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
