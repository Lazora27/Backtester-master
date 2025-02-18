import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
