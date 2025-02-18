import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
