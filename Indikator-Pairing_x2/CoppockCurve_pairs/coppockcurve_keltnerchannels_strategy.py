import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'KeltnerChannels': 1.0
        })
    )
