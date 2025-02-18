import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
