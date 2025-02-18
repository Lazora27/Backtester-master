import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'AverageTrueRange': 1.0
        })
    )
