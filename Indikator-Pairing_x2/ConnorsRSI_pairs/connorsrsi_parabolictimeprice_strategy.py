import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
