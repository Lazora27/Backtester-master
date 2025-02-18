import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und NVISignals
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'NVISignals': 1.0
        })
    )
