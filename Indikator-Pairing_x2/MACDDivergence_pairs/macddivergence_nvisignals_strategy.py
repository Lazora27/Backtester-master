import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und NVISignals
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'NVISignals': 1.0
        })
    )
