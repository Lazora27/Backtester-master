import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MassIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MassIndex': 1.0
        })
    )
