import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
