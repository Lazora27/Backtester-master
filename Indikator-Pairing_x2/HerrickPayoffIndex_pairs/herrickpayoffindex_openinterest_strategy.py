import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
