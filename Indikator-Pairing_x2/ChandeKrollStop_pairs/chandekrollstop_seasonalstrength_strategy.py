import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'SeasonalStrength': 1.0
        })
    )
