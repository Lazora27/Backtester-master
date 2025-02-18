import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
