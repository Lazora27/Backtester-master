import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
