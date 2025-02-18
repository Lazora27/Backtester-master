import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
