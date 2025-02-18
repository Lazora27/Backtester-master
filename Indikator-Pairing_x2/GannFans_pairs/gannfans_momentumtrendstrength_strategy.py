import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
