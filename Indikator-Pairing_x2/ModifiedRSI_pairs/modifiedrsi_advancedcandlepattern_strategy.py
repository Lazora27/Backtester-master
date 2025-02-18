import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
