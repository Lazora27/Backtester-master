import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
