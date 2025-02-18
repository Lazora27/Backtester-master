import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
