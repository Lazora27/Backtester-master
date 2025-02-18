import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
