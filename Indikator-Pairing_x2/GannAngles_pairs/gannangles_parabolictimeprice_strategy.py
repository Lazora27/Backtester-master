import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
