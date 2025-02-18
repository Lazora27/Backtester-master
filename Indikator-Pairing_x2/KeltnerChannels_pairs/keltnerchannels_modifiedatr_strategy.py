import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'ModifiedATR': 1.0
        })
    )
