import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'KeltnerChannels': 1.0
        })
    )
