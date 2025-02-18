import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
