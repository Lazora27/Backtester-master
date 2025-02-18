import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VolatilityIndex': 1.0
        })
    )
