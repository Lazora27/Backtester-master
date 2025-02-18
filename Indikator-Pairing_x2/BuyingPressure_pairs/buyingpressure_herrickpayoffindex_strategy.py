import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
