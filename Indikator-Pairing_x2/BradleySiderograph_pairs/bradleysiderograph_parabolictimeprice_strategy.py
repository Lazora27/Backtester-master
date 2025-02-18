import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
