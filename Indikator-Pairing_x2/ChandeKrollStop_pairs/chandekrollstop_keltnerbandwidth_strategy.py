import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
