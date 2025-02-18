import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
