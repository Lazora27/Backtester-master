import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
