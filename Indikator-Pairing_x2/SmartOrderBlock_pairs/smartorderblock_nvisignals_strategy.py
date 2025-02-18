import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und NVISignals
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'NVISignals': 1.0
        })
    )
