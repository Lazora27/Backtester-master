import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
