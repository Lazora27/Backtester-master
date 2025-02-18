import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'LiquidityIndex': 1.0
        })
    )
