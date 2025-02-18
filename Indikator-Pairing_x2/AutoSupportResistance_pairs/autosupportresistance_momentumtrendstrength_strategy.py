import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
