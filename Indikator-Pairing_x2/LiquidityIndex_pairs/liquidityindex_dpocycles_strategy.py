import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
