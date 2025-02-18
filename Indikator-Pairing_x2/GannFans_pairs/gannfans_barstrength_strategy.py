import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BarStrength
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BarStrength': 1.0
        })
    )
