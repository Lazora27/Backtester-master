import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
