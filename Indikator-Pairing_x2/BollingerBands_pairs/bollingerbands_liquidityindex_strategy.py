import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'LiquidityIndex': 1.0
        })
    )
